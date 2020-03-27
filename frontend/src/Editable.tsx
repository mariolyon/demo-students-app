import MaterialTable from "material-table";
import React from "react";

interface IProps {
}

interface IState {
    columns: any
}

const studentsService = "http://localhost:5000"

class Editable extends React.PureComponent<IProps, IState> {
    constructor(props: Readonly<{}>) {
        super(props);
        this.state = {
            columns: [
                {title: 'Uuid', field: 'uuid', editable: false},
                {title: 'Class', field: 'class', type: 'numeric'},
                {title: 'Name', field: 'name'},
                {title: 'Sex', field: 'sex', lookup: {'male': 'male', 'female': 'female'}},
                {title: 'Age', field: 'age', type: 'numeric'},
                {title: 'Siblings', field: 'siblings', type: 'numeric'},
                {title: 'Gpa', field: 'gpa', type: 'numeric'},
            ]
        }
    }

    static getStudentDataFrom = (newData: any) => {
        return {
            'class': newData['class'],
            'name': newData['name'],
            'sex': newData['sex'],
            'age': newData['age'],
            'siblings': newData['siblings'],
            'gpa': newData['gpa']
        }
    };

    render() {
        return (
            <MaterialTable
                title="Students"
                columns={this.state.columns}
                data={query =>
                    new Promise((resolve, reject) => {
                        // prepare your data and then call resolve like this:
                        const response = fetch(`${studentsService}/students`);
                        response.then(r =>
                            r.json()
                        ).then(
                            json =>
                                resolve({
                                        data: json,
                                        page: 0,
                                        totalCount: json.length
                                    }
                                )
                        )
                    })
                }
                options={{
                    addRowPosition: 'last',
                    showFirstLastPageButtons: false,
                    search: false,
                    sorting: false,
                    paging: false,
                    actionsColumnIndex: 7
                }}
                editable={{
                    onRowAdd: newData => {
                        return new Promise((resolve, reject) => {
                            // prepare your data and then call resolve like this:
                            const studentData = Editable.getStudentDataFrom(newData)

                            const response = fetch(`${studentsService}/student`,
                                {
                                    method: 'POST',
                                    cache: 'no-cache',
                                    headers: {
                                        'Content-Type': 'application/json',
                                        'mario': 'yes'
                                    },
                                    body: JSON.stringify(studentData)
                                });
                            response
                                .then(r => r.json())
                                .then(json => resolve({
                                    data: json,
                                    page: 0,
                                    totalCount: json.length
                                }))
                        })
                    },
                    onRowUpdate: (newData: any) => {
                        return new Promise((resolve, reject) => {
                            // prepare your data and then call resolve like this:
                            const uuid = newData.uuid
                            const studentData = Editable.getStudentDataFrom(newData)

                            const response = fetch(`${studentsService}/student/${uuid}`,
                                {
                                    method: 'PUT',
                                    cache: 'no-cache',
                                    headers: {
                                        'Content-Type': 'application/json',
                                    },
                                    body: JSON.stringify(studentData)
                                });
                            response
                                .then(r => r.json())
                                .then(json => resolve({
                                    data: json,
                                    page: 0,
                                    totalCount: json.length
                                }))
                        })
                    },
                    onRowDelete: (oldData: any) => {
                        return new Promise((resolve, reject) => {
                            const uuid = oldData.uuid
                            const response = fetch(`${studentsService}/student/${uuid}`,
                                {
                                    method: 'DELETE',
                                    cache: 'no-cache',
                                    headers: {
                                        'Content-Type': 'application/json'
                                    }
                                });
                            response
                                .then(r => r.json())
                                .then(json => resolve({
                                    data: json,
                                    page: 0,
                                    totalCount: json.length
                                }))
                        })
                    },
                }}
            />
        )
    }
}

export default Editable;
