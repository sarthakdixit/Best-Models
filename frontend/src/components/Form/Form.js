import React, {useState, useEffect} from 'react';
import {Documents} from "../../utilities/Documents";

const Form = ({formData, handleChange, handleFileChange, handleSubmit, loading}) => {
    const [disable, setDisable] = useState(true);
    const [modelTypeDescription, setModelTypeDescription] = useState("");

    useEffect(() => {
        handleDisable();
        changeDescription();
    }, [formData])

    const changeDescription = () => {
        let arr = Documents.models;
        for(let i=0;i<arr.length;i++){
            if(formData.model_type == arr[i].key){
                setModelTypeDescription(arr[i].description);
                break;
            }
        }
    }

    const handleDisable = () => {
        let arr = Documents.percentForCleaning;
        for(let i=0;i<arr.length;i++){
            if(arr[i] == formData.cleaning_data_type){
                setDisable(false);
                return;
            }
        }
        setDisable(true);
    }

  return (
    <form onSubmit={handleSubmit}>
  <div className="form-row">
    <div className="form-group col-md-6">
      <label htmlFor="models">Models</label>
      <select id="models" name="model_type" className="form-control" value={formData.model_type} onChange={handleChange}>
        <option value="">Choose...</option>
        {Documents.models.map((item, id) => {
            return <option value={item.key} key={id}>{item.value}</option>
        })}
      </select>
      <small>{modelTypeDescription}</small>
    </div>
    <div className="form-group col-md-6">
    <label htmlFor="cleaningModel">Cleaning Model</label>
      <select id="cleaningModel" name="cleaning_data_type" className="form-control" value={formData.cleaning_data_type} onChange={handleChange}>
        <option value="">Choose...</option>
        {Documents.cleaningModels.map((item, id) => {
            return <option value={item.key} key={id}>{item.value}</option>
        })}
      </select>
    </div>
  </div>

  <div className="form-row">
  <div className="form-group col-md-6">
    <label htmlFor="encodingModel">Encoding Model</label>
      <select id="encodingModel" name="encoding_type" className="form-control" value={formData.encoding_type} onChange={handleChange}>
        <option value="">Choose...</option>
        {Documents.encodingModels.map((item, id) => {
            return <option value={item.key} key={id}>{item.value}</option>
        })}
      </select>
    </div>
    <div className="form-group col-md-6">
    <label htmlFor="percentNum">Percent Num</label>
    <input type="number" className="form-control" min={0} id="percentNum" name="percent_num" value={formData.percent_num} onChange={handleChange} disabled={disable} />
    </div>
    <div className="form-group col-md-6">
    <label htmlFor="discardedColumns">Discarded Columns</label>
    <input type="text" className="form-control" id="discardedColumns" name="discarded_columns" value={formData.discarded_columns} onChange={handleChange} />
    <small>Input columns name seperated by ',' to remove from process. If you want none of them to remove than use 'no-col'</small>
    </div>
    <div className="form-group col-md-6">
    <label htmlFor="label">Label</label>
    <input type="text" className="form-control" id="label" name="label" value={formData.label} onChange={handleChange} />
    <small>Input column name which you want as label</small>
    </div>
    
  </div>
  <div className="form-group col-md-3">
    <label htmlFor="exampleFormControlFile1">Choose .csv file</label>
    <input type="file" className="form-control-file" id="exampleFormControlFile1" onChange={handleFileChange} />
  </div>
  
  <button type="submit" className="btn btn-primary" disabled={loading}>Submit</button>
</form>
  )
}

export default Form