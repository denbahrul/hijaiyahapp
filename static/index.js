(function()
{
    var canvas = document.querySelector( "#canvas" );
    var context = canvas.getContext( "2d" );
    var canvasStyle = getComputedStyle(canvas);
    canvas.width = parseInt(canvasStyle.width, 10);
    canvas.height = parseInt(canvasStyle.height, 10);
    var Mouse = { x: 0, y: 0 };
    var lastMouse = { x: 0, y: 0 };
    context.fillStyle="white";
    context.fillRect(0,0,canvas.width,canvas.height);
    context.color = "black";
    context.lineWidth = 15;
    context.lineJoin = context.lineCap = 'round';

    debug();
    canvas.addEventListener( "mousemove", function( e )
    {
    lastMouse.x = Mouse.x;
    lastMouse.y = Mouse.y;
    Mouse.x = e.pageX - this.offsetLeft;
    Mouse.y = e.pageY - this.offsetTop;
    }, false );
    canvas.addEventListener( "mousedown", function( e )
    {
    canvas.addEventListener( "mousemove", onPaint, false );
    }, false );
    canvas.addEventListener( "mouseup", function()
    {
    canvas.removeEventListener( "mousemove", onPaint, false );
    }, false );

    // Event mousemove dengan touchmove untuk perangkat mobile
    canvas.addEventListener("touchmove", function(e) {
        e.preventDefault(); // Mencegah scroll default
        var touch = e.touches[0];
        lastMouse.x = Mouse.x;
        lastMouse.y = Mouse.y;
        Mouse.x = touch.pageX - this.offsetLeft;
        Mouse.y = touch.pageY - this.offsetTop;
    }, false);

    // Event mousedown dengan touchstart untuk perangkat mobile
    canvas.addEventListener("touchstart", function(e) {
        e.preventDefault();
        var touch = e.touches[0];
        Mouse.x = touch.pageX - this.offsetLeft;
        Mouse.y = touch.pageY - this.offsetTop;
        lastMouse.x = Mouse.x;
        lastMouse.y = Mouse.y;
        canvas.addEventListener("touchmove", onPaint, false);
    }, false);

    // Event mouseup dengan touchend untuk perangkat mobile
    canvas.addEventListener("touchend", function() {
        canvas.removeEventListener("touchmove", onPaint, false);
    }, false);

    var onPaint = function()
    {  
    context.lineWidth = context.lineWidth;
    context.lineJoin = "round";
    context.lineCap = "round";
    context.strokeStyle = context.color;

    context.beginPath();
    context.moveTo( lastMouse.x, lastMouse.y );
    context.lineTo( Mouse.x, Mouse.y );
    context.closePath();
    context.stroke();
    };
    function debug()
    {
    /* CLEAR BUTTON */
    var clearButton = $( "#clearButton" );

    clearButton.on( "click", function()
    {
        
        context.clearRect( 0, 0, 664, 373 );
        context.fillStyle="white";
        context.fillRect(0,0,canvas.width,canvas.height);
        
    });

    /* LINE WIDTH */
    var slider = document.getElementById("myRange");
    var output = document.getElementById("sliderValue");
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
        context.lineWidth = $( this ).val();
    }

    $( "#lineWidth" ).change(function()
    {
        context.lineWidth = $( this ).val();
    });
    }
}());