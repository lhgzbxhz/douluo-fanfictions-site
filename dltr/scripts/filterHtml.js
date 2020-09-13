function filterHtml(str) {
    str = str.replace(/<\/?[^>]*>/g, ''); //去除HTML Tag
    str = str.replace(/[|]*\n/, '');      //去除行尾空格
    str = str.replace(/&npsp;/ig, '');    //去除npsp
    return str;
}