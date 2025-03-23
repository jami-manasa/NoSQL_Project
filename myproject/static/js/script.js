// // Toggle Password Visibility
// function togglePassword() {
//     let passwordField = document.getElementById('password');
//     if (passwordField.type === 'password') {
//         passwordField.type = 'text';
//     } else {
//         passwordField.type = 'password';
//     }
// }
// Toggle Password Visibility
function togglePassword() {
    let passwordField = document.getElementById('password');
    passwordField.type = passwordField.type === 'password' ? 'text' : 'password';
}

$(document).ready(function () {
    // 🌟 Sidebar Toggle Functionality
    $("#toggle-sidebar").click(function () {
        $("#sidebar").toggleClass("collapsed");
        $("#content").toggleClass("collapsed");
    });

    // 📌 Load content dynamically using AJAX when clicking sidebar links
    $(".nav-link").click(function (e) {
        e.preventDefault(); // Prevent default link behavior
        var url = $(this).attr("data-url");

        // Show loading animation while fetching data
        $("#dynamic-content").html("<p style='text-align:center; color:#555;'>Loading...</p>");

        $.ajax({
            url: url,
            type: "GET",
            dataType: "html",
            success: function (data) {
                $("#dynamic-content").html(data);
            },
            error: function () {
                $("#dynamic-content").html("<p style='color: red; text-align:center;'>Error loading content.</p>");
            }
        });
    });

    // 🌙 Dark Mode Toggle (With Local Storage)
    if (localStorage.getItem("darkMode") === "enabled") {
        $("body").addClass("dark-mode");
        $("#sidebar").addClass("dark");
        $("#darkModeToggle").prop("checked", true);
    }

    $("#darkModeToggle").change(function () {
        $("body").toggleClass("dark-mode");
        $("#sidebar").toggleClass("dark");

        // Save user preference
        if ($("body").hasClass("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
        } else {
            localStorage.setItem("darkMode", "disabled");
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded successfully"); // ✅ Debugging Check

    function confirmLogout(event) {
        event.preventDefault(); // Prevent default link behavior

        // Remove any existing popups before creating a new one
        let existingPopup = document.querySelector(".logout-popup");
        if (existingPopup) {
            existingPopup.remove();
        }

        console.log("Logout button clicked!"); // ✅ Debugging Check

        // Create confirmation box dynamically
        let confirmBox = document.createElement("div");
        confirmBox.classList.add("logout-popup");
        confirmBox.innerHTML = `
            <div class="logout-popup-content">
                <p>Are you sure you want to logout?</p>
                <div class="logout-buttons">
                    <button id="logout-yes">Yes</button>
                    <button id="logout-no">No</button>
                </div>
            </div>
        `;
        document.body.appendChild(confirmBox);

        // Show popup
        confirmBox.style.display = "block";

        // ✅ Add event listeners inside confirmLogout function
        document.getElementById("logout-yes").addEventListener("click", function () {
            console.log("Logout confirmed"); // ✅ Debugging Check
            window.location.href = "/logout/"; // Ensure this URL is correct
        });

        document.getElementById("logout-no").addEventListener("click", function () {
            console.log("Logout canceled"); // ✅ Debugging Check
            confirmBox.remove();
        });
    }

    // ✅ Attach event listener only when the element exists
    let logoutButton = document.getElementById("logout-button");
    if (logoutButton) {
        console.log("Logout button found:", logoutButton); // ✅ Debugging Check
        logoutButton.addEventListener("click", confirmLogout);
    } else {
        console.error("Logout button NOT found!");
    }
});

// chat bot 