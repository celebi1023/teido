import React, { useState } from 'react';
import RegressionDisplay from './Regression.js'

function FileUpload() {
    // State to store uploaded file
    const [file, setFile] = React.useState("");
    const [fileExists, setFileExists] = React.useState(false);
    const [data, setData] = useState({});
  
    // Handles file upload event and updates state
    function handleUpload(event) {
      if(event.target.files.length === 0){
        setFileExists(false);
      }
      else{
        setFile(event.target.files[0]);
        setFileExists(true);
      }
    }

    function process() {
        const newData = new FormData();
        newData.append('file', file);
        newData.append('filename', file.name);
        const requestOptions = {
            method: 'POST',
            body: newData
        };
        const api = fetch('/reg', requestOptions)
                      .then(response => response.json())
                      .then(newData => setData(newData));
    }
  
    return (
      <div id="upload-box">
        {
            fileExists ? 
            <div>
                <RegressionDisplay data = {data}/>
                <p>Filename: {file.name}</p>
                <p>File type: {file.type.substring(12)}</p>
            </div> : 
            <div>
               
            </div>
        }
        <input type="file" onChange={handleUpload} />
        <button onClick={process}>
            Submit
        </button>
      </div>
    );
  }

  export default FileUpload;