const wakatime = fetch('https://wakatime.com/share/@c3419dbf-0038-499d-9d18-532e0b87876f/5936d31f-1414-404c-a67b-98f15a6dbb51.json')
  .then(response => {response.json(); console.log(response.json());});

let ctx = document.getElementById('coding-chart');

let data = {
    datasets: [{
        data: [10, 20, 30],
        backgroundColor: ['rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 206, 86, 0.7)']
    }],
    labels: ['Red','Yellow','Blue']
};

Chart.defaults.global.defaultFontSize = 40;
Chart.defaults.global.defaultFontFamily = "'Asap', sans-serif";

let myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: data
});
