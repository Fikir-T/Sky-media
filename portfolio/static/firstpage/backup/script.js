document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector(".btn");

    button.addEventListener("mouseover", function () {
        button.style.transform = "scale(1.1)";
    });

    button.addEventListener("mouseout", function () {
        button.style.transform = "scale(1)";
    });

    console.log("JavaScript is loaded and running!");
});
document.addEventListener("DOMContentLoaded", function () {
    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            document.getElementById(targetId).scrollIntoView({
                behavior: "smooth"
            });
        });
    });

    // Hover effect on button
    const button = document.querySelector(".btn");
    button.addEventListener("mouseover", function () {
        this.style.transform = "scale(1.1)";
    });
    button.addEventListener("mouseout", function () {
        this.style.transform = "scale(1)";
    });

    // Hover effect on service boxes
    document.querySelectorAll(".service").forEach(service => {
        service.addEventListener("mouseover", function () {
            this.style.boxShadow = "0px 0px 15px rgba(0, 123, 255, 0.7)";
        });
        service.addEventListener("mouseout", function () {
            this.style.boxShadow = "none";
        });
    });
});
