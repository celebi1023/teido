import React from "react";
import {Bar} from 'react-chartjs-2';

function RegressionDisplay(props) {
    if(!props.data["unique kanji count"]){
        return null
    }

    const state = {
        labels: ['N5', 'N4', 'N3','N2', 'N1'],
        datasets: [
          {
            label: 'Unique Kanji',
            backgroundColor: 'rgba(75,192,192,1)',
            borderColor: 'rgba(0,0,0,1)',
            borderWidth: 2,
            data: props.data["unique kanji count"]
          }
        ]
    }

    //console.log(props.data)

    return (
      <div id="regression-data">
        <Bar
          data={state}
          options={{
            title:{
              display:true,
              text:'Average Rainfall per month',
              fontSize:20
            },
            legend:{
              display:true,
              position:'right'
            }
          }}
        />
      </div>
    );
  }

  export default RegressionDisplay;