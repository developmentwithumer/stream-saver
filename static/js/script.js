const shareButton = document.getElementById('share-button');
const shareButtonMobile = document.getElementById('share-button-mobile');

const title = document.title;
const url = document.location.href;

shareButton.addEventListener('click', () => {
    if (navigator.share) {
        navigator.share({
            title: title,
            text: "Check out this amazing web app that allows to download videos from almost any source.",
            url: url,
        })
            .then(() => console.log('Successful share'))
            .catch((error) => console.log('Error sharing', error));
    } else {
        console.log('Web Share API not supported.');
    }
});

shareButtonMobile.addEventListener('click', () => {
    if (navigator.share) {
        navigator.share({
            title: title,
            text: "Check out this amazing web app that allows to download videos from almost any source.",
            url: url,
        })
            .then(() => console.log('Successful share'))
            .catch((error) => console.log('Error sharing', error));
    } else {
        console.log('Web Share API not supported.');
    }
});

const hamburger = document.querySelector('.hamburger');
const hamburgerClose = document.querySelector('.hamburger-close');
const hamburgerOpen = document.querySelector('.hamburger-open');
const header = document.querySelector('#header');
const nav = document.querySelector('#mobile-nav');

hamburger.addEventListener('click', () => {
    header.classList.toggle("fixed");

    const isNavOpen = nav.classList.contains('flex-imp');

    hamburgerClose.classList.toggle('hidden-imp');
    hamburgerOpen.classList.toggle('block-imp');


    if (!isNavOpen) {
        nav.classList.add('flex-imp');
        setTimeout(() => {
            nav.classList.add('translate-x-imp');
        }, 200);
    } else {
        nav.classList.remove('translate-x-imp');
        setTimeout(() => {
            nav.classList.remove('flex-imp');
        }, 300);
    }
});

function closeMenu() {
    const isNavOpen = nav.classList.contains('flex-imp');

    hamburgerClose.classList.remove('hidden-imp');
    hamburgerOpen.classList.remove('block-imp');

    if(isNavOpen) {
        nav.classList.remove('translate-x-imp');
        setTimeout(() => {
            nav.classList.remove('flex-imp');
        }, 300);
    }
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
        closeMenu();
    }
});

document.addEventListener('click', (event) => {
    if (!nav.contains(event.target) && !hamburger.contains(event.target)) {
        closeMenu();
    }
});

const navItems = document.querySelectorAll('.nav-item');
navItems.forEach((item) => {
    item.addEventListener('click', () => {
        closeMenu();
    });
});

