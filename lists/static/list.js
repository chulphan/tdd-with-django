window.Tddtutorial = {};
window.Tddtutorial.initialize = function() {
    $('input[name="text"]').on('keypress', function() {
        $('.has-error').hide();
    })
}