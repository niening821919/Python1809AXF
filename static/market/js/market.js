$(function () {
    $('.market').width(innerWidth)
    //  获取cookie
    typeIndex = $.cookie('typeIndex')
    if (typeIndex) { // 已经有点击
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    } else { // 没有点击分类
        $('.type-slider .type-item:first').addClass('active')
    }


    $('.type-item').click(function () {
        //  设置cookie
        $.cookie('typeIndex', $(this).index(), {expires: 3, path: '/'})

    })


    // # 分类 按钮
    categoryBt = false
    $('#categoryBt').click(function () {
        categoryBt = !categoryBt

        categoryBt ? categoryviewShow() : categoryviewHide()
    })


    // # 排序 按钮

    sortBt = false
    $('#sortBt').click(function () {
        sortBt = !sortBt

        sortBt ? sortviewShow() : sortviewHide()

    })

    // 灰色蒙层
    $('.bounce-view').click(function () {
        categoryBt = false
        categoryviewHide()
        sortBt = false
        sortviewHide()
    })


    function categoryviewShow() {
        sortBt = false
        sortviewHide()
        $('.bounce-view.category-view').show()
        $('#categoryBt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
    }
    function categoryviewHide() {
        $('.bounce-view.category-view').hide()
        $('#categoryBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    }

    function sortviewShow() {
        categoryBt = false
        categoryviewHide()
        $('.bounce-view.sort-view').show()
        $('#sortBt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
    }
    function sortviewHide() {
        $('.bounce-view.sort-view').hide()
        $('#sortBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    }

})


