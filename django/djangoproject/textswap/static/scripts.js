

$(document).ready(function() {
    // Function to filter apartment listings based on form inputs
    function filterListings() {
        var sublet = $('#sublet').val() || null;
        var minPrice = $('#minPrice').val() || '';
        var maxPrice = $('#maxPrice').val() || '';
        var priceRange = (minPrice && maxPrice) ? `${minPrice}-${maxPrice}` : '';
        var dishwasher = $('#dishwasher').val() || null;
        var moveDateStart = $('#moveDateStart').val() || null;
        var moveDateEnd = $('#moveDateEnd').val() || null;
        var petsAllowed = $('#petsAllowed').val() || null;
        var numBeds = $('#numBeds').val() || null;
        var numBaths = $('#numBaths').val() || null;
    
        $.ajax({
            url: '/filtered_apartments/',
            method: 'GET',
            data: {
                sublet: sublet,
                price_range: priceRange,
                dishwasher: dishwasher,
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

    

    // Handle form submission to trigger filtering
    $('#filterForm').submit(function(e) {
        e.preventDefault(); // Prevent form submission
        filterListings(); // Filter listings
    });

    // Initially filter listings with default values
    filterListings();

    // Function to reset all filters
    function resetFilters() {
        console.log("Hello, world!");

        // Reset form fields to their default values
        $('#sublet').val('');
        $('#minPrice').val('');
        $('#maxPrice').val('');
        $('#dishwasher').val('');
        $('#moveDateStart').val('');
        $('#moveDateEnd').val('');
        $('#petsAllowed').val('');
        $('#numBeds').val('');
        $('#numBaths').val('');
        $('#washer_dryer').val(''); // Add this line to reset the washer_dryer filter

        // Call filterListings function to update the listings
        filterListings();
    }
    const resetFiltersButton = document.getElementById('resetFiltersButton');

    resetFiltersButton.addEventListener('click', resetFilters);
    // Bind the resetFilters function to the "Reset Filters" button click event
    // $('.btn-secondary:contains("Reset Filters")').click(resetFilters);
    // document.getElementById('resetFiltersButton').addEventListener('click', resetFilters);
    
});