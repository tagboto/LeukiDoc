var viewPatientIcon = $('#viewPatientIcon');
var editPatientIcon = $('#modifyPatientIcon');
var deletePatientIcon = $('#deletePatientIcon');
var patientCollectionCard = $('#patientDataCard');
var patientPage = $('#patientPage');

$(document).ready(function() {
    $('.modal').modal();
    var profile = $('.profile');
    var profileOpt = $('.option');
    var profileOptions = $('.profileInfo');

    patientCollectionCard.click(function() {
        $(this).hide();
        patientPage.show();
    });

    profile.click(function() {
        profileOptions.toggle(200);

    });

    profileOpt.click(function() {
        profileOptions.hide(200);
        var logOutProcess = { logoutBtn: 'clicked' };


    });

    editPatientIcon.click(function() {
        $('#patientEditMod').modal('open');
    });

    viewPatientIcon.click(function() {
        $('#viewPatientMod').modal('open');
    });

    chartCreation();



});


function callAjax(dataArray) {

    $.ajax({

        url: '',

        type: 'POST',

        data: dataArray,

        dataType: 'json',

        success: function(response) {
            console.log('Got em');
            console.log(response);

        },

        error: function() {
            console.log('Got nunin');
        }




    });
}

function chartCreation() {
    var ctx = document.getElementById("leukiGraph");
    var dataL = {
        labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        datasets: [{
            label: "Chemodose",
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(75,192,192,0.4)",
            borderColor: "rgba(75,192,192,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(75,192,192,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(75,192,192,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data: [10, 2.0, 1.0, 0.6666666666666666, 0.5, 0.4, 0.3333333333333333, 0.2857142857142857, 0.25, 0.2222222222222222, 0.2, 0.18181818181818182, 0.16666666666666666, 0.15384615384615385, 0.14285714285714285, 0.13333333333333333, 0.125, 0.11764705882352941, 0.1111111111111111, 0.10526315789473684, 0.1],
            spanGaps: false,
        }]
    };
    var myChart = new Chart(ctx, {
        type: 'line',
        data: dataL,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}