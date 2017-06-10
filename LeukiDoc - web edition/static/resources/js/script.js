 $(function() {
                    $('addBtn').click(function() {
                        var fname = $('#fname').val();
                        var lname = $('#lname').val();
                        var age = $('#age').val();
                        var weight = $('#weight').val();
                        var height = $('#height').val();
                        var rbc = $('#rbc').val();
                        var wbc = $('#wbc').val();
                        var protein = $('#protein').val();
                        var platelets = $('#platelets').val();
                        var chemodose = $('#chemodose').val();
                        $.ajax({

                            url: 'http://127.0.0.1:8080/add',
                            data: $('form').serialize(),
                            type: 'POST',
                            success: function(response) {
                                console.log(response);
                            },
                            error: function(error) {
                                console.log(error);
                            }
                        });
                    });
                });