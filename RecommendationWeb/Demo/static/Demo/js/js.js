const wrapper = document.querySelector(".wrapper"),
selectBtn = wrapper.querySelector(".select-btn"),
searchInp = wrapper.querySelector("input"),
options = wrapper.querySelector(".options");
universityhtml = options.querySelector("li");
//Array of university
let university = ["UEH", "FPT", "Hutech", "USSH", "UIT", "UTE", "UTC2", "UTH"];

function addUni() {
    options.innerHTML ="";
    universityhtml.forEach(uni =>{
        //if selected uni and uni value is same then add selected class
        //let isSelected = uni == selectedCountry ? "selected" : "";
        //adding each uni inside li and inserting all li inside
        let li = `<li>${uni}</li>`;
        options.insertAdjacentHTML("beforeend", li);
    });
}

searchInp.addEventListener("keyup", () =>{
    let arr = [];
    let searchedVal = searchInp.value.toLowerCase();
    //returning all uni from arr which are start with user searched value
    arr = university.filter(data => {
        return data.toLowerCase().startsWith(searchedVal);
    }).map(data => `<li><a href="home1.html">${data}</a></li>`).join("");
    options.innerHTML = arr ? arr : `<p>Không có kết quả</p>`
    
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
majorhtml = nav.querySelector(".options-1");
let major = ["Công nghệ thông tin", "Kinh tế - Tài chính", "Công an - Quân đội", "Ngoại giao - Ngoại ngữ", "Sư phạm - Giáo dục", 
    "Kế toán - Kiểm toán", "Y - Dược", "Xây dựng - Kiến trúc - Giao thông"]
function addMaj() {
    majorhtml.forEach(maj =>{
        //adding each uni inside li and inserting all li inside
        let li = `<li>${maj}</li>`;
        options_1.insertAdjacentHTML("beforeend", li);
    })
}

searchInp_1.addEventListener("keyup", () =>{
    let arr1 = [];
    let searchedVal1 = searchInp_1.value.toLowerCase();
    //returning all uni from arr which are start with user searched value
    arr1 = major.filter(data => {
        return data.toLowerCase().startsWith(searchedVal1);
    }).map(data => `<li> <a href="home1.html">${data}</a></li>`).join("");
    options_1.innerHTML = arr1 ? arr1 : `<p>Không có kết quả</p>`
})

selectBtn_1.addEventListener("click", () => {
    nav.classList.toggle("active")
})

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

// Lấy tất cả các droplist trong sidebar
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
});

// Lấy phần tử input và tất cả các phần tử nhóm ngành
const input = document.getElementById('input-sb');
const allFields = document.querySelectorAll('.select-sidebar');

// Thêm sự kiện khi người dùng nhập vào ô tìm kiếm
input.addEventListener('input', function() {
    const filter = input.value.toLowerCase(); // Chuyển tất cả chữ cái sang chữ thường

    allFields.forEach(field => {
        const text = field.innerText.toLowerCase();
        if (text.includes(filter)) {
            field.parentElement.style.display = ''; // Hiển thị nhóm ngành phù hợp
        } else {
            field.parentElement.style.display = 'none'; // Ẩn nhóm ngành không phù hợp
        }
    });
});