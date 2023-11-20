import React, { useState, useEffect } from 'react';
import Results from './Results';

export const Home = () => {

    const [ctryState, setctryState] = useState(false);
    const [date, setDate] = useState('');
    const [georange, setGeorange] = useState('');
    const [country, setCountry] = useState('Belgium');
    const [numtop, setNumtop] = useState(1);
    const [ascentop, setAscentop] = useState('');
    const [data, setData] = useState(null);

    const handleSubmit =  (e) => {
        e.preventDefault();
        console.log(date, georange, country, numtop, ascentop)
      };



    return (
    <div>
        <div className="text-center">
            <h1 className="mt-3-ce">Enter your search</h1>
            <p>Welcome to our Google Trends application! Please complete the following form 
              to explore the ranking of the current top trends. Simply provide the required 
              information and discover what's at the forefront of trends right now.</p>
        </div>
        <div className="formulario p-4 m-3 border rounded-3">

            <form action="reserva_insert.php" method="post" className="form-group" onSubmit={handleSubmit}>

                <div className="mb-3">
                    <label htmlFor="date" className="form-label">Date</label>
                    <input type="date" className="form-control" id="date" name="date" onChange={(e) => setDate(e.target.value)} required></input>
                </div>

                <div className="my-3">
                    <label htmlFor="search_range" className="form-label">Search range</label>
                    <div className="form-check">
                      <input id="us" name="georange" type="radio" className="form-check-input" onClick={(e) => {setctryState(false); setGeorange(e.target.id)}} required />
                      <label className="form-check-label" htmlFor="us">US</label>
                    </div>
                    <div className="form-check">
                      <input id="intr" name="georange" type="radio" className="form-check-input" onClick={(e) => {setctryState(true); setGeorange(e.target.id)}} required />
                      <label className="form-check-label" htmlFor="intr">International</label>
                    </div>
                </div>

                <div className="mb-3">
                    <label htmlFor="countryselect" className="form-label">Country</label>
                    {ctryState ? (<select name="countryselect" id="countryselect" className="form-select" onChange={(e) => setCountry(e.target.value)} required>
                        
                        <option value="Belgium">Belgium</option>
                        <option value="Israel">Israel</option>
                        <option value="United Kingdom">United Kingdom</option>
                        <option value="Argentina">Argentina</option>
                        <option value="Austria">Austria</option>
                        <option value="Australia">Australia</option>
                        <option value="Brazil">Brazil</option>
                        <option value="Canada">Canada</option>
                        <option value="Switzerland">Switzerland</option>
                        <option value="Chile">Chile</option>
                        <option value="Colombia">Colombia</option>
                        <option value="Czech Republic">Czech Republic</option>
                        <option value="Germany">Germany</option>
                        <option value="Denmark">Denmark</option>
                        <option value="Egypt">Egypt</option>
                        <option value="Finland">Finland</option>
                        <option value="France">France</option>
                        <option value="Hungary">Hungary</option>
                        <option value="Indonesia">Indonesia</option>
                        <option value="India">India</option>
                        <option value="Italy">Italy</option>
                        <option value="Japan">Japan</option>
                        <option value="South Korea">South Korea</option>
                        <option value="Mexico">Mexico</option>
                        <option value="Malaysia">Malaysia</option>
                        <option value="Nigeria">Nigeria</option>
                        <option value="Netherlands">Netherlands</option>
                        <option value="Norway">Norway</option>
                        <option value="New Zealand">New Zealand</option>
                        <option value="Philippines">Philippines</option>
                        <option value="Poland">Poland</option>
                        <option value="Portugal">Portugal</option>
                        <option value="Romania">Romania</option>
                        <option value="Saudi">Saudi Arabia</option>
                        <option value="Sweden">Sweden</option>
                        <option value="Thailand">Thailand</option>
                        <option value="Turkey">Turkey</option>
                        <option value="Taiwan">Taiwan</option>
                        <option value="Ukraine">Ukraine</option>
                        <option value="Vietnam">Vietnam</option>
                        <option value="South Africa">South Africa</option>
                    </select>) 
                    : (<select name="countryselect" id="countryselect" className="form-select" onChange={(e) => setCountry(e.target.value)}>
                            <option value=""></option>
                    </select>)}
                    
                </div>

                <div className="mb-3">
                    <label htmlFor="numtop" className="form-label">Search top</label>
                    <select name="numtop" id="numtop" className="form-select" onChange={(e) => setNumtop(e.target.value)} required>
                        
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                        <option value="11">11</option>
                        <option value="12">12</option>
                        <option value="13">13</option>
                        <option value="13">13</option>
                        <option value="15">15</option>
                        <option value="16">16</option>
                        <option value="17">17</option>
                        <option value="18">18</option>
                        <option value="19">19</option>
                        <option value="20">20</option>
                        <option value="21">21</option>
                        <option value="22">22</option>
                        <option value="23">23</option>
                        <option value="24">24</option>
                        <option value="25">25</option>
                    </select>
                </div>
                
                <div className="my-3">
                    <label htmlFor="search_range" className="form-label">Top or Rising</label>
                    <div className="form-check">
                      <input id="" name="ascentop" type="radio" className="form-check-input" onClick={(e) => {setAscentop(e.target.id)}} required />
                      <label className="form-check-label" htmlFor="top">Top</label>
                    </div>
                    <div className="form-check">
                      <input id="rising_" name="ascentop" type="radio" className="form-check-input" onClick={(e) => {setAscentop(e.target.id)}} required />
                      <label className="form-check-label" htmlFor="ascen">Rising</label>
                    </div>
                </div>

                <button type="submit" className="btn btn-primary" onClick={() => {// Realiza la solicitud fetch a la API
                                                                                    try {
                                                                                      fetch(`http://127.0.0.1:8000/bigquery/consult?date=${date}&georange=${georange}&country=${country}&numtop=${numtop}&ascentop=${ascentop}&id_post=0`)
                                                                                      .then((response) => response.json())
                                                                                      .then((data) => setData(data[0]));
                                                                                    
                                                                                    } catch (error) {
                                                                                      console.error('Error al hacer la solicitud:', error);
                                                                                    }}}>
                                                                    Search</button>
            </form>
        </div>
        {data != null? (<Results data={data}/>) : (<></>)}
    </div>
  );
};

export default Home;