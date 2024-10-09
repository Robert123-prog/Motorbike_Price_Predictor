document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Gather form data
        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            year: formData.get('year'),
            seller_type: formData.get('seller_type'),
            owner: formData.get('owner'),
            km_driven: formData.get('km_driven'),
            ex_showroom_price: formData.get('ex_showroom_price')
        };

        // Send the data to the back end
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.json();
            })
            .then(result => {
                // Handle the result here
                alert(`The predicted selling price is: ${result.predicted_price}`);
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while predicting the price. Please try again.');
            });
    });
});