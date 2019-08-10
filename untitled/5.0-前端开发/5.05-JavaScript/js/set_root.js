/**
 * Created by Administrator on 2019/6/16.
 */

(function () {
    var calc = function () {
        var docElement = document.documentElement;
        var clientWidthValue = docElement.clentWidth > 750 ? 750 : docElement.clientWidth;
        docElement.style.fontSize = 20*(clientWidthValue/375)+'px';
    }
    calc();
    window.addEventListener('resize',calc)

})();