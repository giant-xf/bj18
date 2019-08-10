$(function(){
	
	var $li = $('.slide_pics li');
	var len = $li.length;
	var $prev = $('.prev');
	var $next = $('.next');
	var timer = null;
	var $slide =$('.slide');
	//将要运动过来的li
	var nowli =0;
	//当前将要离开的li
	var prevli =0;

	//除第一个外，其他的css样式中left赋值760；
	$li.not(':first').css({left:760});

	//循环赋值，有几张图就赋几个点，达到动态设点效果
	$li.each(function(index){

		var $sli = $('<li>');

		if ($(this).index()==0) {

			$sli.addClass('active');
		}

		$sli.appendTo('.points');

	});
	//此时赋值必须放在循环后面，否则没有效果
	var $points = $('.points li');

	//点击points达到播放效果
	$points.click(function(){
		nowli = $(this).index();
		move();
		$(this).addClass('active').siblings().removeClass('active');
	});

	//向前播放
	$prev.click(function(){
		nowli--;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});
	//向后播放
	$next.click(function(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});

	$slide.mouseover(function(){
		clearInterval(timer);
	})
	
	$slide.mouseout(function(){
		timer = setInterval(autoplay,3000);
	})

	timer = setInterval(autoplay,3000);

	//自动播放函数
	function autoplay(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	}

	//移动函数
	function move(){

		//单击同一个图的points直接返回
		if (nowli==prevli) {
			return;
		}

		//极端情况:当向左滑动到顶时
		if (nowli<0) {
			nowli = len-1;
			prevli= 0;
			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
			$li.eq(nowli).stop().animate({left:0});
			prevli = nowli;
			return;
		}

		//极端情况:当向右滑动到顶时
		if (nowli>len-1) {
			nowli = 0;
			prevli= len-1;
			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});
			$li.eq(nowli).stop().animate({left:0});
			prevli = nowli;
			return;
		}

		//向左向右滑动时
		if (nowli>prevli) {

			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});
			
		}

		else{

			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
		}
		$li.eq(nowli).stop().animate({left:0});
		//将赋值给prevli
		prevli = nowli;
	}




})