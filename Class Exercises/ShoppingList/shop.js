const form = document.getElementById('cerealform')
const list = document.getElementById('inStock')
const input = document.getElementById('cereal')

form.addEventListener('submit', function(event) {
    // Create a new element when someone submits a cereal input as item onto list
    event.preventDefault();
    // Pervent the page to refresh after submitting
    const newCereal = document.createElement('li');
    newCereal.innerText = cereal.value;
    list.append(newCereal);
    form.reset();

})
