var seriesData = [];

fetch("/average_gas_fees") // Adjust the route based on your Flask app
  .then((response) => response.json())
  .then((data) => {
    for (var address in data) {
      var addressData = data[address];
      var addressSeries = {
        name: address,
        data: Object.values(addressData),
      };
      seriesData.push(addressSeries);
      console.log(seriesData);
      const chart = Highcharts.chart("container", {
        title: {
          text: "Best time to buy NFTs - Gas fees/Time(USD)",
          align: "left",
        },

        subtitle: {
          text: 'Source: <a href="https://etherscan.io/" target="_blank">Etherscan</a>.',
          align: "left",
        },

        yAxis: {
          title: {
            text: "Price",
          },
        },

        xAxis: {
          type: "datetime",
          tickInterval: 1,
          labels: {
            format: "{value}:00", // Format hours
          },
        },

        legend: {
          layout: "vertical",
          align: "right",
          verticalAlign: "middle",
        },

        plotOptions: {
          series: {
            label: {
              connectorAllowed: false,
            },
            pointStart: 0,
          },
        },

        series: seriesData,

        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 500,
              },
              chartOptions: {
                legend: {
                  layout: "horizontal",
                  align: "center",
                  verticalAlign: "bottom",
                },
              },
            },
          ],
        },
      });
      document.getElementById("loading").style.display = "none";
    }
  });
