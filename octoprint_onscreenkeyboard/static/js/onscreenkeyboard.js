$(function() {
    //Attach keyboard to all input elements.
    $("input[type='number']").keyboard({
        usePreview: false,
        autoAccept: true,
        layout: "num"
    });
    $("input[type='text']").keyboard({
      usePreview: false,
      autoAccept: true,
    });
});
