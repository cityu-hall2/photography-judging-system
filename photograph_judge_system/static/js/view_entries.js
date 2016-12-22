$(function() {
    // rank
    function initial_rank() {
        var list = $('.sortable')[0];
        var items = list.childNodes;
        var itemsArr = [];
        for (var i in items) {
            if (items[i].nodeType == 1) {
                itemsArr.push(items[i]);
            }
        }

        itemsArr.sort(function(a, b) {
          return parseInt(a.getAttribute('data-rank')) == parseInt(b.getAttribute('data-rank'))
                  ? 0
                  : (parseInt(a.getAttribute('data-rank')) > parseInt(b.getAttribute('data-rank'))? 1 : -1);
        });

        for (i = 0; i < itemsArr.length; ++i) {
          list.appendChild(itemsArr[i]);
        }
    }
    function update_ranks() {
        var list = $('.sortable')[0];
        var items = list.childNodes;
        var under_the_line = false;
        var index = 0;
        for (var i = 0; i < items.length; ++i) {
            if (items[i].nodeType == 1) {
                if ($(items[i]).hasClass('rank-split')) {
                    under_the_line = true;
                } else {
                    if (under_the_line) {
                        $(items[i]).css('background-color', 'grey');
                        $('#rank-form > input[name=' + $(items[i]).attr('data-id') + ']').val(10000);
                    } else {
                        $(items[i]).css('background-color', 'transparent');
                        $('#rank-form > input[name=' + $(items[i]).attr('data-id') + ']').val(index);
                    }
                }
                index++;
            }
        }
    }
    initial_rank();
    update_ranks();
    $('.sortable').sortable().bind('sortupdate', function() {
        update_ranks();
    });

    // gallery
    $('.gallery').each(function() {
        $(this).magnificPopup({
            delegate: 'a',
            type: 'image',
            gallery: {
              enabled:true
            }
        });
    })
});