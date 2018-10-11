package com.kddi.android.UtaPass.sqa_espresso.pages.library;

import com.kddi.android.UtaPass.R;
import com.kddi.android.UtaPass.sqa_espresso.common.BasicButton;
import com.kddi.android.UtaPass.sqa_espresso.pages.common.BasicPage;
import com.kddi.android.UtaPass.sqa_espresso.pages.library.myplaylist.CreatNowButton;
import com.kddi.android.UtaPass.sqa_espresso.pages.library.myplaylist.CreatPlaylistPage;
import com.kddi.android.UtaPass.sqa_espresso.pages.library.myplaylist.MyplaylistUp;
import com.kddi.android.UtaPass.sqa_espresso.pages.library.myplaylist.SortButton;
import com.kddi.android.UtaPass.sqa_espresso.pages.library.myplaylist.SortMenu;

import static android.support.test.espresso.matcher.ViewMatchers.withId;

public class MyPlaylistPage extends BasicPage{
    private BasicButton backBtn;


    public CreatNowButton creatNowButton(){
        return new CreatNowButton();
    }

    public MyplaylistUp myplaylistlineUp(){
        return new MyplaylistUp();
    }

    public SortButton sortButton(){
        return new SortButton();
    }

    public SortMenu sortMenu(){
        return new SortMenu();
    }

    public BasicButton backButton(){
        if( this.backBtn == null ) {
            this.backBtn = new BasicButton( () -> withId(R.id.main_drawer_icon) );
        }
        return this.backBtn;
    }

    public CreatPlaylistPage creatPlaylistPage(){
        return new CreatPlaylistPage();
    }

}
