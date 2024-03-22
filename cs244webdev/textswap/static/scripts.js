$(document).ready(function() {
    // Function to filter apartment listings based on form inputs
    function filterListings() {
        var sublet = $('#sublet').val();
        var minPrice = $('#minPrice').val();
        var maxPrice = $('#maxPrice').val();
        var dishwasher = $('#dishwasher').val();
        var washer_dryer = $('#washer_dryer').val();
        var moveDateStart = $('#moveDateStart').val();
        var moveDateEnd = $('#moveDateEnd').val();
        var petsAllowed = $('#petsAllowed').val();
        var numBeds = $('#numBeds').val();
        var numBaths = $('#numBaths').val();
    
        $.ajax({
            url: '/filtered_apartments/',
            method: 'GET',
            data: {
                sublet: sublet,
                minPrice: minPrice,
                maxPrice: maxPrice,
                dishwasher: dishwasher,
                washer_dryer: washer_dryer,
                move_date_start: moveDateStart,
                move_date_end: moveDateEnd,
                pets_allowed: petsAllowed,
                num_beds: numBeds,
                num_baths: numBaths
            },
            success: function(response) {
                $('#listings').html(response.apartments_html);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    }

    // Function to reset all filters
    function resetFilters() {
        $('#filterForm')[0].reset(); // Reset form
        filterListings(); // Filter listings with default values
    }

    // Handle form submission to trigger filtering
    $('#filterForm').submit(function(e) {
        e.preventDefault(); // Prevent form submission
        filterListings(); // Filter listings
    });

    // Initially filter listings with default values
    filterListings();
});