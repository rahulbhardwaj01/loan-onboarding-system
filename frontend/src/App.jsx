import React, { useState } from 'react';

const API_URL = 'http://127.0.0.1:8000/api';

function App() {
  const [formData, setFormData] = useState({
    amount: '', term: '', firstName: '', lastName: '', email: '', street: '', city: '', state: '', zipCode: '',
  });
  const [searchQuery, setSearchQuery] = useState('');
  const [loanDetails, setLoanDetails] = useState(null);
  const [transformedJson, setTransformedJson] = useState(null);
  const [xmlData, setXmlData] = useState('');
  const [message, setMessage] = useState('');

  const handleFormChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleCreateLoan = async (e) => {
    e.preventDefault();
    setMessage('');
    const payload = {
      amount: formData.amount,
      term: formData.term,
      customers: [{
        first_name: formData.firstName,
        last_name: formData.lastName,
        email: formData.email,
        address: { street: formData.street, city: formData.city, state: formData.state, zip_code: formData.zipCode },
      }],
    };
    try {
      const response = await fetch(`${API_URL}/loans/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      if (!response.ok) throw new Error('Failed to create loan.');
      const result = await response.json();
      setMessage(`Loan created successfully! Loan Number: ${result.loan_number}`);
      setSearchQuery(result.loan_number);
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    }
  };

  const handleSearchLoan = async (e) => {
    e.preventDefault();
    setMessage('');
    setLoanDetails(null);
    setTransformedJson(null);
    setXmlData('');
    if (!searchQuery) {
      setMessage('Please enter a Loan Number to search.');
      return;
    }

    try {
      const [detailsRes, jsonRes, xmlRes] = await Promise.all([
        fetch(`${API_URL}/loans/${searchQuery}/`),
        fetch(`${API_URL}/loans/${searchQuery}/json/`),
        fetch(`${API_URL}/loans/${searchQuery}/xml/`),
      ]);
      if (!detailsRes.ok) throw new Error('Could not find loan details.');
      const detailsData = await detailsRes.json();
      const jsonData = await jsonRes.json();
      const xmlText = await xmlRes.text();
      setLoanDetails(detailsData);
      setTransformedJson(jsonData);
      setXmlData(xmlText);
    } catch (error) {
      setMessage(`Error: ${error.message}`);
    }
  };

  return (
    <div className="container my-5">
      <h1 className="text-center mb-4">🏦 Loan Onboarding System</h1>

      <div className="card mb-4">
        <div className="card-header"><h2>Create a New Loan</h2></div>
        <div className="card-body">
          <form onSubmit={handleCreateLoan}>
            <div className="row g-3">
              <div className="col-md-6"><label htmlFor="amount" className="form-label">Loan Amount</label><input id="amount" name="amount" value={formData.amount} onChange={handleFormChange} placeholder="50000" className="form-control" required /></div>
              <div className="col-md-6"><label htmlFor="term" className="form-label">Loan Term (months)</label><input id="term" name="term" value={formData.term} onChange={handleFormChange} placeholder="36" className="form-control" required /></div>
              <div className="col-md-6"><label htmlFor="firstName" className="form-label">First Name</label><input id="firstName" name="firstName" value={formData.firstName} onChange={handleFormChange} placeholder="Rahul" className="form-control" required /></div>
              <div className="col-md-6"><label htmlFor="lastName" className="form-label">Last Name</label><input id="lastName" name="lastName" value={formData.lastName} onChange={handleFormChange} placeholder="Bhardwaj" className="form-control" required /></div>
              <div className="col-12"><label htmlFor="email" className="form-label">Email</label><input id="email" name="email" type="email" value={formData.email} onChange={handleFormChange} placeholder="rahul@example.com" className="form-control" required /></div>
              <div className="col-12"><label htmlFor="street" className="form-label">Street</label><input id="street" name="street" value={formData.street} onChange={handleFormChange} placeholder="" className="form-control" required /></div>
              <div className="col-md-6"><label htmlFor="city" className="form-label">City</label><input id="city" name="city" value={formData.city} onChange={handleFormChange} placeholder="chandigarhh" className="form-control" required /></div>
              <div className="col-md-4"><label htmlFor="state" className="form-label">State</label><input id="state" name="state" value={formData.state} onChange={handleFormChange} placeholder="chandigarh" className="form-control" required /></div>
              <div className="col-md-2"><label htmlFor="zipCode" className="form-label">Zip Code</label><input id="zipCode" name="zipCode" value={formData.zipCode} onChange={handleFormChange} placeholder="12345" className="form-control" required /></div>
            </div>
            <button type="submit" className="btn btn-primary mt-3">Create Loan</button>
          </form>
        </div>
      </div>

      <div className="card mb-4">
        <div className="card-header"><h2>Search for a Loan</h2></div>
        <div className="card-body">
          <form onSubmit={handleSearchLoan} className="d-flex">
            <input type="text" value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} className="form-control me-2" placeholder="Enter Loan Number..." />
            <button type="submit" className="btn btn-success">Search</button>
          </form>
        </div>
      </div>
      
      {message && <div className="alert alert-info">{message}</div>}

      {loanDetails && (
        <div className="row">
          <div className="col-lg-4 mb-3"><h3>Raw JSON Response</h3><pre className="bg-dark text-white p-3 rounded">{JSON.stringify(loanDetails, null, 2)}</pre></div>
          <div className="col-lg-4 mb-3"><h3>Transformed JSON</h3><pre className="bg-dark text-white p-3 rounded">{JSON.stringify(transformedJson, null, 2)}</pre></div>
          <div className="col-lg-4 mb-3"><h3>Generated XML</h3><pre className="bg-dark text-white p-3 rounded">{xmlData}</pre></div>
          {/* JSON.stringify() to format the string with line breaks and use two spaces for each level of nesting, */}
        </div>
      )}
    </div>
  );
}

export default App;