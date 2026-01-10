import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/workouts/')
      .then(res => res.json())
      .then(data => {
        setWorkouts(data.results || data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching workouts:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="card shadow-sm mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Workouts</h2>
        {loading ? (
          <div className="text-center">Loading...</div>
        ) : (
          <div className="table-responsive">
            <table className="table table-striped table-bordered">
              <thead className="table-primary">
                <tr>
                  <th>ID</th>
                  <th>Name</th>
                  <th>Type</th>
                  <th>Duration</th>
                  <th>Intensity</th>
                </tr>
              </thead>
              <tbody>
                {workouts.map((workout, idx) => (
                  <tr key={workout.id || idx}>
                    <td>{workout.id || idx}</td>
                    <td>{workout.name || ''}</td>
                    <td>{workout.type || ''}</td>
                    <td>{workout.duration || ''}</td>
                    <td>{workout.intensity || ''}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default Workouts;

// -8000.app.github.dev/api/workouts/
