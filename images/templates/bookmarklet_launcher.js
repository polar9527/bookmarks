/**
 * Created by polar.
 * ec2-52-78-179-108.ap-northeast-2.compute.amazonaws.com
 */
(function(){
    if(window.myBookmarklet!==undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).
            src='http://www.bookmarks.com/static/images/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();