//TODO: MOCK DATA - Dynamically fetch the data
const user_nft_projects = [
    {name: 'Cryptopunks',
    data:[43934, 48656, 65165, 81827, 112143, 142383, 171533, 165174, 155157, 161454, 154610]},
    {name: 'MutantApe',
    data: [24916, 37941, 29742, 29851, 32490, 30282, 38121, 36885, 33726, 34243, 31050]}]
document.addEventListener('DOMContentLoaded', function () {
        const chart = Highcharts.chart('container', {
    title: {
        text: 'Best time to buy NFTs - Gas fees/Time(USD)',
        align: 'left'
    },

    subtitle: {
        text: 'Source: <a href="https://etherscan.io/" target="_blank">Etherscan</a>.',
        align: 'left'
    },

    yAxis: {
        title: {
            text: 'Price'
        }
    },

    xAxis: {
        type: 'datetime',
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 00
        }
    },

    series: user_nft_projects,

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});
});