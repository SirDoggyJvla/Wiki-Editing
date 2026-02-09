/* Any JavaScript here will be loaded for all users on every page load. */


/** 
 * Test if an element has a certain class 
 * 
 * Description: Uses regular expressions and caching for better performance.
 * Maintainers: [[User:Mike Dillon]], [[User:R. Koot]], [[User:SG]] 
 *   
var hasClass = ( function() {
	var reCache = {};
	return function( element, className ) {
		return ( reCache[className] ? reCache[className] : ( reCache[className] = new RegExp( "(?:\\s|^)" + className + "(?:\\s|$)" ) ) ).test( element.className );
	};
})();
** */

/**
 * Test if an element has a certain class
 * @deprecated:  Use $(element).hasClass() instead.
 */
mw.log.deprecate( window, 'hasClass', function ( element, className ) {
	return $( element ).hasClass( className );
}, 'Use jQuery.hasClass() instead' );

/* Template:Infobox/image */
window.addOnloadHook(function() {
  $('.infobox-image .infobox-gallery > *:first-child img').addClass('selected');
  $('.infobox-preview:first-child').show();
  $('.infobox-image .infobox-gallery > *').click(function() {
    var index = $(this).index();
    var previews = $(this).closest('.infobox-image').find('.infobox-preview');
    if (index < previews.length) {
      $(this).parent().find('img').removeClass('selected');
      $(this).find('img').addClass('selected');
      previews.hide();
      $(previews[index]).show();
    }
  });
});

/* Cycle through images with cycle-img */
window.addOnloadHook(function() {
    var cycleContainers = $('.cycle-img');
    cycleContainers.each(function() {
        var images = $(this).children('span[typeof="mw:File"]');
        if (images.length > 1) {
            var currentIndex = 0;
            images.eq(currentIndex).show();
            images.slice(1).hide();
            function switchImage() {
                images.eq(currentIndex).hide();
                currentIndex = (currentIndex + 1) % images.length;
                images.eq(currentIndex).show();
            }
            setInterval(switchImage, 2000);
        }
    });
});

/* Choice selector box - show/hide content based on user selection */
window.addOnloadHook(function() {
    $('.choice-box').each(function() {
        var box = $(this);
        var choices = box.find('.choice-selector .mw-ui-button');
        var contents = box.find('.choice-content');

        // Hide all content except the first
        contents.hide();
        contents.eq(0).show();

        // Mark first button as active
        choices.eq(0).addClass('active');

        // Add click handlers
        choices.on('click', function() {
            var index = choices.index(this); // <-- FIX

            choices.removeClass('active');
            $(this).addClass('active');

            contents.hide();
            contents.eq(index).show();
        });
    });
});

/* Template:Info (icon tooltip) */
window.addOnloadHook(function() {
    $(".tooltip-info-img").on("mouseover touchstart", function(e) {
        var tooltip = $(this).siblings('.tooltip-info-text');
        var windowWidth = $(window).width();

        if (windowWidth <= 600) {
            // Small screen
            var imageRect = $(this)[0].getBoundingClientRect();
            var tooltipHeight = tooltip.outerHeight();
            var tooltipWidth = tooltip.outerWidth();
            var tipY, tipX;

            if (imageRect.top > tooltipHeight + 10) {
                tipY = imageRect.top - tooltipHeight - 10;
            } else {
                tipY = imageRect.bottom + 10;
            }

            tooltip.css({
                top: tipY,
                left: tipX
            });
        } else {
            // Large screen
            var tooltip = $(this).siblings('.tooltip-info-text'); // Get tooltip element (tooltip-text)
            var tipX = $(this).outerWidth() + 5;             // 5px on the right of the tooltip
            var tipY = -40;                                  // 40px on the top of the tooltip
            tooltip.css({ top: tipY, left: tipX });          // Position tooltip

            // Get calculated tooltip coordinates and size
            var tooltip_rect = tooltip[0].getBoundingClientRect();
            // Corrections if out of window
            if ((tooltip_rect.x + tooltip_rect.width) > $(window).width()) { // Out on the right
                tipX = -tooltip_rect.width - 5; // Simulate a "right: tipX" position
            }
            if (tooltip_rect.y < 0) { // Out on the top
                tipY = tipY - tooltip_rect.y + 10; // Align on the top
            }

            // Apply corrected position
            tooltip.css({ top: tipY, left: tipX });
        }
    });
});
