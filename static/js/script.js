$(document).ready(function() {

    $("#create-beer_style").modalForm({
        formURL: "{% url 'add_review' %}"
    });

});