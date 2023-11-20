
const Results = (props) => {

  return (
    <div className="tabla mt-5 mx-3 rounded-3 overflow-hidden">
            
            {Object.keys(props.data).length > 0 ? (
                <table className="table table-striped table-bordered">
                <thead className="table-dark">
                  <tr>
                    <th scope="col" className="text-center">Term</th>
                    <th scope="col" className="text-center">Rank</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.keys(props.data).map((key) => (
                    <tr key={key}>
                      <td className="text-center">{key}</td>
                      <td className="text-center">{props.data[key]}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
        ) : <p>There is no data for the date entered, try a different date.</p>}

    </div>
  );
};

export default Results;