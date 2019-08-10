/**
 * Created by Administrator on 2019/6/21.
 */


window.onload = function () {


    var oMask = document.getElementById('mask');
    var oSpan = document.getElementById('span');
    var oMask1 = document.getElementById('mask1');
    var oBtn2 = document.getElementById('btn2');
    var oBtn1 = document.getElementById('btn1');
    var oBtn3 = document.getElementById('btn3');


    oMask.style.display = 'none';







    oBtn3.onclick = function () {
        function timeleft() {

        if (oSpan.innerHTML == 0) {
            oMask.style.display = 'none';
            clearsetInterval(timeleft)
        }
        oSpan.innerHTML = oSpan.innerHTML * 1 - 1;
    }


    // timeleft();
     setInterval(timeleft, 1000);
    }

    oBtn2.onclick = function () {
        oMask1.style.display = 'block';
    };

    oBtn1.onclick = function () {
        var left = -300;
        var bottom = 300;
        var a =100;
        var b =600;
        var num1 = Math.random()*(b-a)+a;
        var num2 = Math.random()*(b-a)+a;
        // alert(oBtn1.style.left);
        oBtn1.style.left = (left+num1)/40 + 'rem';
        oBtn1.style.bottom = (bottom-num2)/40 + 'rem';
    };

















};
