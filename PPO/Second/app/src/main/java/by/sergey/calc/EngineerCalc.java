package by.sergey.calc;

public class EngineerCalc extends Calc{
    private static EngineerCalc calc;

    public static EngineerCalc getCalc(){
        if (calc == null){
            calc = new EngineerCalc();
        }
        return calc;
    }

    private EngineerCalc(){

    }

    @Override
    public String addDigit(String digit) {
        if (number.length() >= maxLength)
            return number;
        if (number.length() > 0 && Double.parseDouble(number) == 0 && !number.contains("."))
            number = "";
        return number += digit;
    }

    @Override
    public boolean setEqual() {
        try {
            switch (this.operation.toLowerCase()) {
                case "+":
                    number = String.valueOf(Double.parseDouble(memory) + Double.parseDouble(number));
                    break;
                case "-":
                    number = String.valueOf(Double.parseDouble(memory) - Double.parseDouble(number));
                    break;
                case "*":
                    number = String.valueOf(Double.parseDouble(memory) * Double.parseDouble(number));
                    break;
                case "x^y":
                    number = String.valueOf(Math.pow(Double.parseDouble(memory), Double.parseDouble(number)));
                    break;
                case "/":
                    if (Double.parseDouble(number) == 0) {
                        return false;
                    }
                    number = String.valueOf(Double.parseDouble(memory) / Double.parseDouble(number));
                    break;
                default:
                    return false;
            }
            this.operation = "";
            memory = "";
            return true;
        }catch (Exception e){
            return false;
        }
    }

    @Override
    public String changeSign() {
        if (number.length() > 0 && Double.parseDouble(number) == 0)
            return number;
        if (number.startsWith("-")) {
            number = number.substring(1);
        } else {
            number = "-" + number;
        }
        return number;
    }

    public String addDot(){
        if (!number.contains(".")){
            number += '.';
        }
        return number;
    }

    public boolean UnaryOperation(String operation){
        try {
            switch (operation.toLowerCase()) {
                case "sin":
                    number = String.valueOf(Math.sin(Double.parseDouble(number))).substring(0, 10);
                    break;
                case "cos":
                    number = String.valueOf(Math.cos(Double.parseDouble(number))).substring(0, 10);
                    break;
                case "tan":
                    number = String.valueOf(Math.tan(Double.parseDouble(number))).substring(0, 10);
                    break;
                case "sqrt":
                    number = String.valueOf(Math.sqrt(Double.parseDouble(number)));
                    break;
                default:
                    return false;
            }
            if (number.length() > 10) {
                number = number.substring(0, 10);
            }
            return true;
        }catch (Exception e){
            return false;
        }
    }
}
