$(function() {
    $('.carousel').carousel({
        interval: 5000 //changes the speed
    });

    var cbpAnimatedHeader = (function() {

        var docElem = document.documentElement,
            header = $('.navbar-default'),
            didScroll = false,
            changeHeaderOn = 300;

        function init() {
            window.addEventListener( 'scroll', function( event ) {
                if( !didScroll ) {
                    didScroll = true;
                    setTimeout( scrollPage, 250 );
                }
            }, false );
        }

        function scrollPage() {
            var sy = scrollY();
            if ( sy >= changeHeaderOn ) {
                header.addClass('navbar-shrink');
            }
            else {
                header.removeClass('navbar-shrink');
            }
            didScroll = false;
        }

        function scrollY() {
            return window.pageYOffset || docElem.scrollTop;
        }

        init();

    })();

    $("#services .col-md-4").waypoint({
        handler: function(direction) {
            $(this.element).addClass('animated fadeInDown');
        },
        offset: 'bottom-in-view'
    });
});