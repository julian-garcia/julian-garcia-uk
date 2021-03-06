// Render a chart using the Chart.js framework
// The languages object was generated by the python index view which
// fetched my coding activity via the Wakatime API

let data_array = [];
let label_array = [];
let colour_array = [];

for (let language in languages) {
  let red_component = Math.floor(Math.random() * 256);
  let green_component = Math.floor(Math.random() * 256);
  let blue_component = Math.floor(Math.random() * 256);
  let colour = `rgba(${red_component}, ${green_component}, ${blue_component}, 1)`;
  data_array.push(languages[language]);
  label_array.push(language);
  colour_array.push(colour);
}

let ctx = document.getElementById('coding-chart');

let data = {
    datasets: [{
        data: data_array,
        backgroundColor: colour_array
    }],
    labels: label_array
};

Chart.defaults.global.defaultFontSize = 40;
Chart.defaults.global.defaultFontFamily = "'Asap', sans-serif";

let myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: data
});
