jsx
// BulkUpdateForm.jsx

import React, { useState } from 'react';
import axios from 'axios';

const BulkUpdateForm = () => {
  const [updateType, setUpdateType] = useState('employee');
  const [fileFormat, setFileFormat] = useState('csv');
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('update_type', updateType);
    formData.append('file_format', fileFormat);
    formData.append('file', file);

    axios.post('/api/bulk-update', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
      .then((response) => {
        console.log(response.data.message);
        // Handle success
      })
      .catch((error) => {
        console.error(error);
        // Handle error
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Update Type:
        <select value={updateType} onChange={(e) => setUpdateType(e.target.value)}>
          <option value="employee">Employee</option>
          <option value="company">Company</option>
        </select>
      </label>

      <label>
        File Format:
        <select value={fileFormat} onChange={(e) => setFileFormat(e.target.value)}>
          <option value="csv">CSV</option>
          <option value="text">Text</option>
          <option value="excel">Excel</option>
        </select>
      </label>

      <input type="file" onChange={handleFileChange} />

      <button type="submit">Submit</button>
    </form>
  );
};