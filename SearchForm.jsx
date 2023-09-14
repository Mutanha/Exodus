// SearchForm.jsx

import React, { useState } from 'react';
import axios from 'axios';

const SearchForm = () => {
  const [name, setName] = useState('');
  const [employer, setEmployer] = useState('');
  const [position, setPosition] = useState('');
  const [department, setDepartment] = useState('');
  const [yearStarted, setYearStarted] = useState('');
  const [yearLeft, setYearLeft] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const params = {
      name,
      employer,
      position,
      department,
      year_started: yearStarted,
      year_left: yearLeft,
    };

    axios.get('/api/search-employees', { params })
      .then((response) => {
        console.log(response.data.results);
        // Handle search results
      })
      .catch((error) => {
        console.error(error);
        // Handle error
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Render form fields for each search criterion */}
      <button type="submit">Search</button>
    </form>
  );
};
