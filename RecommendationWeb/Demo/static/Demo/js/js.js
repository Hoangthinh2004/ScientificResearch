const wrapper = document.querySelector(".wrapper"),
selectBtn = wrapper.querySelector(".select-btn"),
searchInp = wrapper.querySelector("input"),
options = wrapper.querySelector(".options");
//universityhtml = options.querySelector("li");
const university_set = wrapper.querySelectorAll(".option-u");
//Array of university
let university = Array.from(university_set).map(item => ({
    id: item.dataset.universityId,
    name: item.dataset.universityName,
    url: item.dataset.universityUrl
}));

// function addUni() {
//     options.innerHTML ="";
//     universityhtml.forEach(uni =>{
//         //if selected uni and uni value is same then add selected class
//         //let isSelected = uni == selectedCountry ? "selected" : "";
//         //adding each uni inside li and inserting all li inside
//         let li = `<li>${uni}</li>`;
//         options.insertAdjacentHTML("beforeend", li);
//     });
// }

// searchInp.addEventListener("keyup", () =>{
//     let arr = [];
//     let searchedVal = searchInp.value.toLowerCase();
//     //returning all uni from arr which are start with user searched value
//     arr = university.filter(data => {
//         // Check if the input is found anywhere within either the university ID or name
//         return data.name.toLowerCase().includes(searchedVal) || data.id.toLowerCase().includes(searchedVal);
//     }).map(data => `<li><a href="{% url 'show-one-university'${data.id} %}">${data.id}-${data.name}</a></li>`).join("");
//     options.innerHTML = arr ? arr : `<p>Không có kết quả</p>`
    
// });

searchInp.addEventListener("keyup", () => {
    let searchedVal = searchInp.value.toLowerCase();

    // Filter and display universities
    let filteredUnis = university.filter(data => {
        return data.name.toLowerCase().includes(searchedVal) || data.id.toLowerCase().includes(searchedVal);
    });

    // Update the options list
    options.innerHTML = filteredUnis.length ? 
        filteredUnis.map(data => `<li><a href="${data.url}">${data.id}-${data.name}</a></li>`).join("") :
        `<p>Không có kết quả</p>`;
});

selectBtn.addEventListener("click", () => {
    wrapper.classList.toggle("active");
});

document.addEventListener("click", (e) => {
    if (!wrapper.contains(e.target)) {
        wrapper.classList.remove("active");
    }
    
});

//nav-1
const nav = document.querySelector(".nav-1"),
      selectBtn_1 = nav.querySelector(".select-btn-1"),
      searchInp_1 = nav.querySelector("input"),
      options_1 = nav.querySelector(".options-1"),
      major_set = nav.querySelectorAll(".option-m");

let major = Array.from(major_set).map(item => ({
    id: item.dataset.majorId,
    name: item.dataset.majorName,
    url: item.dataset.majorUrl
}));

// searchInp_1.addEventListener("keyup", () => {
//     let arr1 = [];
//     let searchedVal1 = searchInp_1.value.toLowerCase();

//     arr1 = major.filter(data => {
//         // Check if the input is found anywhere within either the major ID or the major name
//         return data.name.toLowerCase().includes(searchedVal1) || data.id.toLowerCase().includes(searchedVal1);
//     }).map(data => `<li><a href="{% url 'show-one-major' %}${data.id}">${data.id}-${data.name}</a></li>`).join("");

//     options_1.innerHTML = arr1 ? arr1 : `<p>Không có kết quả</p>`;
// });

searchInp_1.addEventListener("keyup", () => {
    let searchedVal = searchInp_1.value.toLowerCase();

    // Filter and display universities
    let filteredMajs = major.filter(data => {
        return data.name.toLowerCase().includes(searchedVal) || data.id.toLowerCase().includes(searchedVal);
    });

    // Update the options list
    options_1.innerHTML = filteredMajs.length ? 
        filteredMajs.map(data => `<li><a href="${data.url}">${data.id}-${data.name}</a></li>`).join("") :
        `<p>Không có kết quả</p>`;
});

selectBtn_1.addEventListener("click", () => {
    nav.classList.toggle("active");
});

document.addEventListener("click", (e) => {
    if (!nav.contains(e.target)) {
        nav.classList.remove("active");
    }
});



//Click vào nội dung nhưng checkbox vẫn hoạt động
document.querySelectorAll('.options-sb li').forEach(function(item) {
    item.addEventListener('click', function(event) {
        // Kiểm tra nếu click không phải vào checkbox
        if (event.target.tagName !== 'INPUT') {
            const checkbox = item.querySelector('input[type="checkbox"]');
            checkbox.checked = !checkbox.checked; // Đổi trạng thái checkbox
        }
    });
});

//droplist cho side bar
document.addEventListener('DOMContentLoaded', () => {
    const selects = document.querySelectorAll('.select-sidebar');

    selects.forEach(select => {
        select.addEventListener('click', () => {
            const contentSidebar = select.parentElement;

            // Close other active droplists
            document.querySelectorAll('.content-sidebar.active').forEach(activeSidebar => {
                if (activeSidebar !== contentSidebar) {
                    activeSidebar.classList.remove('active');
                }
            });

            // Toggle 'active' class for current droplist
            contentSidebar.classList.toggle('active');
        });
    });

    // Search filter logic
    const input = document.getElementById('input-sb');
    const allFields = document.querySelectorAll('.content-sidebar');

    input.addEventListener('input', function () {
        const filter = input.value.toLowerCase(); // Convert input to lowercase for case-insensitive search

        allFields.forEach(field => {
            const text = field.querySelector('.select-sidebar span').innerText.toLowerCase();
            if (text.includes(filter)) {
                field.style.display = ''; // Show matching fields
            } else {
                field.style.display = 'none'; // Hide non-matching fields
            }
        });
    });
});


//Filter- bộ lọc 
const selectedFilters = document.querySelector('.selected-filters');
const resetButton = document.getElementById('reset-filters');

// Handle checkbox selection
document.querySelectorAll('.dropdown-content input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        updateSelectedFilters();
    });
});

// Update selected filters display
function updateSelectedFilters() {
    selectedFilters.innerHTML = '';

    const filterGroups = {};

    document.querySelectorAll('.dropdown-content input[type="checkbox"]:checked').forEach(checkbox => {
        const dropdownLabel = checkbox.closest('.filter-item').querySelector('.dropdown-btn').textContent.trim();
        const selectedValue = checkbox.nextSibling.textContent.trim();

        if (!filterGroups[dropdownLabel]) {
            filterGroups[dropdownLabel] = [];
        }
        filterGroups[dropdownLabel].push(selectedValue);
    });

    for (const [label, values] of Object.entries(filterGroups)) {
        const filterTag = document.createElement('span');
        filterTag.textContent = `${label}: ${values.join(', ')}`;
        selectedFilters.appendChild(filterTag);
    }
}

// Reset filters
resetButton.addEventListener('click', function() {
    document.querySelectorAll('.dropdown-content input[type="checkbox"]').forEach(checkbox => {
        checkbox.checked = false;
    });
    selectedFilters.innerHTML = '';
});

// toggle checkbox
document.addEventListener("click", function(event) {
    const checkbox = document.getElementById('check');
    const label = document.querySelector('label[for="check"]');
    if(!checkbox.contains(event.target) && !label.contains(event.target)){
        checkbox.checked = false;
    }
});