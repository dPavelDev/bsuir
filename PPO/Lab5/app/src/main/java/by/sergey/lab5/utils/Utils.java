package by.sergey.lab5.utils;

import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.AdapterView;

import com.mikepenz.materialdrawer.Drawer;
import com.mikepenz.materialdrawer.accountswitcher.AccountHeader;
import com.mikepenz.materialdrawer.model.PrimaryDrawerItem;
import com.mikepenz.materialdrawer.model.interfaces.IDrawerItem;

import by.sergey.lab5.R;
import by.sergey.lab5.fragments.Fragment1;
import by.sergey.lab5.fragments.Fragment2;
import by.sergey.lab5.fragments.Fragment3;

public class Utils {

    public static Drawer.OnDrawerItemClickListener handlerOnClick(final Drawer.Result drawerResult, final FragmentActivity activity) {
        return new Drawer.OnDrawerItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id, IDrawerItem drawerItem) {

                if (drawerItem != null) {

                    if (drawerItem.getIdentifier() == 1) {
                        activity.getSupportFragmentManager().beginTransaction().replace(R.id.frame_container, new Fragment1()).commit();
                    } else if (drawerItem.getIdentifier() == 2) {
                        activity.getSupportFragmentManager().beginTransaction().replace(R.id.frame_container, new Fragment2()).commit();
                    } else if (drawerItem.getIdentifier() == 3) {
                        activity.getSupportFragmentManager().beginTransaction().replace(R.id.frame_container, new Fragment3()).commit();
                    }
                }
            }
        };
    }

    public static Drawer.Result createCommonDrawer(final FragmentActivity activity, Toolbar toolbar, AccountHeader.Result headerResult) {

        Drawer.Result drawerResult = new Drawer()
                .withActivity(activity)
                .withAccountHeader(headerResult)
                .addDrawerItems(
                        new PrimaryDrawerItem().withName(R.string.info_fr1).withIdentifier(1),
                        new PrimaryDrawerItem().withName(R.string.info_fr2).withIdentifier(2),
                        new PrimaryDrawerItem().withName(R.string.info_fr3).withIdentifier(3)
                ).build();

        drawerResult.setOnDrawerItemClickListener(handlerOnClick(drawerResult, activity));

        return drawerResult;
    }

}
