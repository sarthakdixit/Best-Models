import React, {useState} from 'react';
import Form from "./components/Form/Form";
import ResultUI from './components/ResultUI/ResultUI';
import {Config} from "./utilities/Config";

function App() {
  const [formData, setFormData] = useState({
    model_type:"",
    cleaning_data_type:"",
    percent_num:40,
    encoding_type:"",
    discarded_columns:"no-col",
    label:""
  })
  const [file, setFile] = useState();
  const [resultData, setResultData] = useState({});
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false)

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  }

  const handleChange = (e) => {
    let name = e.target.name;
    let value = e.target.value;
    setFormData({
      ...formData,
      [name]: value,
    });
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    setError("");
    setResultData({});
    setLoading(true);

    let data = new FormData();
    data.append("model_type", formData.model_type);
    data.append("cleaning_data_type", formData.cleaning_data_type);
    data.append("percent_num", formData.percent_num);
    data.append("encoding_type", formData.encoding_type);
    data.append("discarded_columns", formData.discarded_columns);
    data.append("label", formData.label);
    data.append("file", file);

    let config = {
      method: 'POST',
      body: data
    }

    try{
      let response = await fetch(Config.baseUrl, config);
      let result = await response.json();
      setResultData(result)
    }catch(e){
      setError(e.message);
    }
    setLoading(false);
  }

  return (
    <div className="App">
      <Form formData={formData} handleChange={handleChange} handleFileChange={handleFileChange} handleSubmit={handleSubmit} loading={loading} />
      <h4 style={{color:"red"}}>{error}</h4>
      <hr/>
      {Object.keys.length != 0 ? <ResultUI resultData={resultData} /> : null}
    </div>
  );
}

export default App;
