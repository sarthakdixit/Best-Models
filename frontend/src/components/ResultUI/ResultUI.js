import React from 'react';
import { Config } from '../../utilities/Config';
import "./index.css";

const ResultUI = ({resultData}) => {
  return (
    <div>
        {resultData.hasOwnProperty("heatmap") ? <div className='img-container'>
            <h3>Heatmap</h3>
        <img src={`${Config.baseUrl}/${resultData.heatmap}`} />
        </div> : null}

        {resultData.hasOwnProperty("pairplot") ? <div className='img-container'>
            <h3>Pairplot</h3>
        <img src={`${Config.baseUrl}/${resultData.pairplot}`} />
        </div> : null}

        {resultData.hasOwnProperty("scatter_plot") ? <div className='img-container'>
            <h3>Scatter Plot</h3>
        <img src={`${Config.baseUrl}/${resultData.scatter_plot}`} />
        </div> : null}

        <br></br>
        {resultData.hasOwnProperty("intercept") ? <div className='img-container'>
            <h5>Intercept : {resultData.intercept}</h5>
        </div> : null}

        {resultData.hasOwnProperty("score") ? <div className='img-container'>
            <h5>Score : {resultData.score}</h5>
        </div> : null}

        {resultData.hasOwnProperty("rmse") ? <div className='img-container'>
            <h5>Root Mean Square : {resultData.rmse}</h5>
        </div> : null}

        {resultData.hasOwnProperty("r-squared") ? <div className='img-container'>
            <h5>R Squared : {resultData["r-squared"]}</h5>
        </div> : null}
    </div>
  )
}

export default ResultUI