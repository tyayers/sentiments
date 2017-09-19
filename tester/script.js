var cogUrl = "http://cogsentia.azurewebsites.net/v1/analytics";
var pyUrl = "http://pysenti.azurewebsites.net/v1/analytics";

//var cogUrl = "http://tylerswarmagents.westeurope.cloudapp.azure.com:443/v1/analytics";
//var pyUrl = "http://tylerswarmagents.westeurope.cloudapp.azure.com:80/v1/analytics";
//var pyUrl = "http://localhost:8081/v1/analytics";

//var pyUrl_de = "http://localhost:8081/v1/analytics";

var openWebRequests = 0;

$( document ).ready(function() {
    console.log( "ready!" );

    setGuauge("cogguage", 0);
    setGuauge("pyguage", 0);
});

function submit() {
    var text = $("#textInput").val();
    openWebRequests = 2;
    var langRadioValue = $('input[name=langCodeRadio]:checked').val();
    $("#p2").show();

    var request = {
        "language-code": langRadioValue,
        "customer-text": text
    };

    $.ajax({
        url: cogUrl,
        type: 'post',
        data: JSON.stringify(request),
        headers: {
            "Content-Type": 'application/json'   //If your header name has spaces or any other char not appropriate
        },
        dataType: 'json',
        success: function (data) {
            console.info(data);
            openWebRequests = openWebRequests - 1;
            if (openWebRequests <= 0)
                $("#p2").hide();

            var sentimentWhole = data["sentiment-score"] * 100;

            $("#cogserv-results").html(getSentimentDescription(sentimentWhole));

            setGuauge("cogguage", sentimentWhole);            
        },
        error: function(data) {
            openWebRequests = openWebRequests - 1;
            if (openWebRequests <= 0)
                $("#p2").hide();      

            $("#cogserv-results").html("Unfortunately an error occurred while contacting the service. ");
            setGuauge("cogguage", 0);
        }
    });

    // var realPyUrl = pyUrl;
    // if (langRadioValue == "de")
    //     realPyUrl = pyUrl_de;

    $.ajax({
        url: pyUrl,
        type: 'post',
        data: JSON.stringify(request),
        headers: {
            "Content-Type": 'application/json'   //If your header name has spaces or any other char not appropriate
        },
        dataType: 'json',
        success: function (data) {
            console.info(data);
            openWebRequests = openWebRequests - 1;
            if (openWebRequests <= 0)
            $("#p2").hide();

            var sentimentWhole = data["sentiment-score"] * 100;

            $("#pyserv-results").html(getSentimentDescription(sentimentWhole));
            setGuauge("pyguage", sentimentWhole);            
        },
        error: function(data) {
            openWebRequests = openWebRequests - 1;
            if (openWebRequests <= 0)
                $("#p2").hide();        
                
            $("#pyserv-results").html("Unfortunately an error occurred while contacting the service. ");
            setGuauge("pyguage", 0);
        }
    });    
}

function getSentimentDescription(sentimentValue) {
    var result = "";

    if (sentimentValue < 30)
        result = "The text was analyzed to have a sentiment positivity value of <b>" + sentimentValue + "</b>, which is pretty miserable.  This person is not at all happy or content, and is probably very aggressive to other people.";
    else if (sentimentValue < 50) 
        result = "The text was analyzed to have a sentiment positivity value of <b>" + sentimentValue + "</b>, which is mildly aggravated, but not aggressive.  This person is unhappy, but it would be possible to improve their sentiment with positive words and actions.";
    else if (sentimentValue < 80) 
        result = "The text was analyzed to have a sentiment positivity value of <b>" + sentimentValue + "</b>, which is lightly positive.  This person is content but not overly joyous.";
    else 
        result = "The text was analyzed to have a sentiment positivity value of <b>" + sentimentValue + "</b>, which is very positive.  This person is overjoyed and completely happy.";
   
    return result;
}

function setGuauge(guageCanvasId, value) {
    var opts = {
        angle: 0.06, // The span of the gauge arc
        lineWidth: 0.44, // The line thickness
        radiusScale: 1, // Relative radius
        pointer: {
            length: 0.6, // // Relative to gauge radius
            strokeWidth: 0.035, // The thickness
            color: '#000000' // Fill color
        },
        limitMax: false,     // If false, max value increases automatically if value > maxValue
        limitMin: false,     // If true, the min value of the gauge will be fixed
        colorStart: '#FF4081',   // Colors
        colorStop: '#FF4081',    // just experiment with them
        strokeColor: '#E0E0E0',  // to see which ones work best for you
        generateGradient: true,
        highDpiSupport: true     // High resolution support
    };

    var target = document.getElementById(guageCanvasId); // your canvas element
    var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
    gauge.maxValue = 100; // set max gauge value
    gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
    gauge.animationSpeed = 32; // set animation speed (32 is default value)
    gauge.set(value); // set actual value  
}