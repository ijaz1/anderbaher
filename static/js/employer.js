// add hovered class in selected list item

let list = document.querySelectorAll('.navigation li');
function activelink() {
    list.forEach((item) =>
        item.classList.remove('hovered'));
    this.classList.add('hovered')
}
list.forEach((item) =>
    item.addEventListener('mouseover', activelink));

// menu toggle

let toggle = document.querySelector('.toggle');
let navigation = document.querySelector('.navigation');
let main = document.querySelector('.main');

toggle.onclick = function () {
    navigation.classList.toggle('active')
    main.classList.toggle('active')
    toggle.classList.toggle('turn')
}

function rotateToggle() {
    var action = document.querySelector('.toggle');
    action.classList.toggle('turn')

}

const donut = document.getElementById('donut').getContext('2d');
const donutt = document.getElementById('donutt').getContext('2d');
const donuttt = document.getElementById('donuttt').getContext('2d');

const myChart = new Chart(donut, {
    type: 'doughnut',
    data: {
        labels: [
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 50],
            backgroundColor: [
                'rgb(253, 56, 56)',
                'rgb(255, 255, 255)'
            ],
            hoverOffset: 4
        }]
    },
});

const myChartt = new Chart(donutt, {
    type: 'doughnut',
    data: {
        labels: [
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 100],
            backgroundColor: [
                'rgb(224, 255, 45)',
                'rgb(255, 255, 255)'
            ],
            hoverOffset: 4
        }]
    },
});

const myCharttt = new Chart(donuttt, {
    type: 'doughnut',
    data: {
        labels: [
        ],
        datasets: [{
            label: 'My First Dataset',
            data: [300, 100],
            backgroundColor: [
                'rgb(37, 113, 255)',
                'rgb(255, 255, 255)'
            ],
            hoverOffset: 4
        }]
    },
});
