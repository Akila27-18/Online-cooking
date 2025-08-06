// Data for the testimonials
const testimonials = [
    {
        images: "/static/image/Ellipse 7.png",
        text: '"CHEF MADE IT FUN, EVEN FOR A TOTAL BEGINNER LIKE ME!"',
        author: 'CARLOS D'
    },
    {
        images: "/static/image/Ellipse 8.png",
        text: '"I FINALLY LEARNED HOW TO COOK WITHOUT GOOGLING EVERY STEP!"',
        author: 'JASON M'
    },
    {
        images: "/static/image/Ellipse 6.png",
        text: '"LEFT WITH NEW SKILLS AND A FULL BELLY. HIGHLY RECOMMEND!"',
        author: 'MAYA S.'
    }
];

let currentTestimonial = 0;

const testimonialImage = document.getElementById('testimonial-images');
const testimonialText = document.getElementById('testimonial-text');
const testimonialAuthor = document.getElementById('testimonial-author');

function updateTestimonial() {
    const testimonial = testimonials[currentTestimonial];
    
    // Apply animation classes
    testimonialImage.style.animation = 'none';
    testimonialText.style.animation = 'none';
    
    // Trigger reflow to restart animation
    void testimonialImage.offsetWidth;
    void testimonialText.offsetWidth;

    // Apply animation
    testimonialImage.style.animation = 'imageFadeIn 0.5s ease-in-out';
    testimonialText.style.animation = 'textFadeIn 0.8s ease-in-out';

    // Update content after animation
    testimonialImage.src = testimonial.images;
    testimonialText.textContent = testimonial.text;
    testimonialAuthor.textContent = '-' + testimonial.author;
}

function showNextTestimonial() {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    updateTestimonial();
}

function showPrevTestimonial() {
    currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
    updateTestimonial();
}

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    updateTestimonial();
});