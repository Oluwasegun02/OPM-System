import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
    const [portfolios, setPortfolios] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/portfolios/")
            .then((response) => setPortfolios(response.data))
            .catch((error) => console.error(error));
    }, []);

    return (
        <div>
            <h1>Portfolios</h1>
            <ul>
                {portfolios.map((portfolio) => (
                    <li key={portfolio.id}>{portfolio.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default App;
