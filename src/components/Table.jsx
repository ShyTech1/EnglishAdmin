import React from 'react';
import students from '../assets/StudentsData'
import SearchBar from './components/StudentCard';

function Table() {

  
    const mapping = students.map((s) => {
        return(

            <tr >
                
            <td >{s.id}</td>
            <td>{s.last}</td>
            <td>{s.first}</td>
            <td>{s.grade}</td>
            <td>{s.class}</td>
            <td>{s.educator}</td>
            <td>{s.teacher}</td>
            <td>{s.literature}</td>
            <td>{s.module1}</td>
            <td>{s.module2}</td>
            <td>{s.oral}</td>
          </tr>
        )
    });
    console.log(mapping)

    return ( 
        <div dir='rtl' className="container">
            <searchBar />
            <h1>Table</h1>
            <div className="table table-striped  table-hover" >
                <thead>
                <tr>
                        <th>תעודת זהות</th>
                        <th>שם משפחה</th>
                        <th>שם פרטי</th>
                        <th>שכבה</th>
                        <th>מקבילה</th>
                        <th>מחנך</th>
                        <th>מורה</th>
                        <th>הע"ח</th>
                        <th>שאלון 1</th>
                        <th>שאלון 2</th>
                        <th>דבורה</th>
                </tr>
                </thead>
                <tbody>
                {mapping}
                </tbody>
            </div>
        </div>
     );
}

export default Table;