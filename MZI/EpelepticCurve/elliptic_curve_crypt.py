def inv(n, q):
    for i in range(q):
        if (n * i) % q == 1:
            return i


def sqrt(n, q):
    assert n < q
    for i in range(1, q):
        if pow(i, 2, q) == n:
            return i, q - i


class EllipticCurve:
    def __init__(self, a, b, p):
        assert (4 * a ** 3 + 27 * b ** 2) % p != 0
        self.a = a
        self.b = b
        self.p = p

    def point_at(self, x):
        ysq = (x ** 3 + self.a * x + self.b) % self.p
        y, my = sqrt(ysq, self.p)
        return EllipticCurvePoint(self, x, y), EllipticCurvePoint(self, x, my)

    def __str__(self):
        return 'a = {}, b = {}, p = {}'.format(self.a, self.b, self.p)


class EllipticCurvePoint:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y

    @property
    def is_zero_point(self):
        return self.x == 0 and self.y == 0

    @property
    def is_valid_point(self):
        if self.is_zero_point:
            return True
        l = self.y ** 2 % self.curve.p
        r = (self.x ** 3 + self.curve.a * self.x + self.curve.b) % self.curve.p
        return l == r

    @property
    def order(self):
        assert self.is_valid_point and not self.is_zero_point
        for i in range(1, self.curve.p + 1):
            if (self * i).is_zero_point:
                return i

    def __neg__(self):
        return EllipticCurvePoint(self.curve, self.x, -self.y % self.curve.p)

    def __add__(self, other):
        if (self.x, self.y) == (0, 0):
            return other
        if (other.x, other.y) == (0, 0):
            return EllipticCurvePoint(self.curve, self.x, self.y)
        if self.x == other.x and (self.y != other.y or self.y == 0):
            return EllipticCurvePoint(self.curve, 0, 0)

        if self.x == other.x:
            l = (3 * self.x ** 2 + self.curve.a) * inv(2 * self.y, self.curve.p) % self.curve.p
        else:
            l = (other.y - self.y) * inv(other.x - self.x, self.curve.p) % self.curve.p

        x = (l * l - self.x - other.x) % self.curve.p
        y = (l * (self.x - x) - self.y) % self.curve.p

        return EllipticCurvePoint(self.curve, x, y)

    def __mul__(self, number):
        result = EllipticCurvePoint(self.curve, 0, 0)
        temp = EllipticCurvePoint(self.curve, self.x, self.y)

        while 0 < number:
            if number & 1 == 1:
                result += temp
            number, temp = number >> 1, temp + temp
        return result

    def __eq__(self, other):
        return (self.curve, self.x, self.y) == (other.curve, other.x, other.y)

    def __str__(self):
        return '({}): x = {}, y = {}'.format(self.curve, self.x, self.y)


class ElGamal:
    def __init__(self, point):
        assert point.is_valid_point
        self.point = point
        self.n = point.order

    def get_public_key(self, private_key):
        return self.point * private_key

    def encrypt(self, data_point, public_key, random_number):
        assert data_point.is_valid_point
        assert public_key.is_valid_point

        return self.point * random_number, data_point + public_key * random_number

    def decrypt(self, data_point_pair, private_key):
        point_first, point_second = data_point_pair
        assert point_first.is_valid_point and point_second.is_valid_point

        return point_second + -(point_first * private_key)


if __name__ == "__main__":
    base_point, _ = EllipticCurve(1, 18, 19).point_at(7)

    chiper = ElGamal(base_point)

    private_key = 5
    public_key = chiper.get_public_key(private_key)
    print('Public', public_key)

    data = base_point * 2
    print('Data', data)
    encrypted = chiper.encrypt(data, public_key, 15)
    print('Encrypted', encrypted[0], encrypted[1])

    decrypted = chiper.decrypt(encrypted, private_key)
    print('Decrypted', decrypted)
    print(decrypted == data)

