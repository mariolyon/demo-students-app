import MaterialTable from "material-table";
import React from "react";

interface IProps {
}

interface IState {
    columns: any,
    data: any
}

class Editable extends React.PureComponent<IProps, IState> {
    constructor(props: Readonly<{}>) {
        super(props);
        this.state = {
            columns: [
                {title: 'Uuid', field: 'uuid'},
                {title: 'Class', field: 'class', initialEditValue: 'initial edit value'},
                {title: 'Name', field: 'name', initialEditValue: 'initial edit value'},
                {
                    title: 'Sex', field: 'sex', lookup: {'male': 'male', 'female': 'female'},
                },
                {title: 'Age', field: 'age', initialEditValue: 'initial edit value'},
                {title: 'Siblings', field: 'siblings', initialEditValue: 'initial edit value'},
                {title: 'Gpa', field: 'gpa', initialEditValue: 'initial edit value'},
            ],
            data: [
                {
                    uuid: '40d6cb1a-fe69-4c11-bdfd-9d2f896f335c',
                    class: '3',
                    name: "Steve Jones",
                    sex: "male",
                    age: '22',
                    siblings: '1'
                },
            ]
        }
    }

    render() {
        return (
            <MaterialTable
                title="Editable Preview"
                columns={this.state.columns}
                data={this.state.data}
                editable={{
                    onRowAdd: newData =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                {
                                    const data = this.state.data;
                                    data.push(newData);
                                    this.setState({data}, () => resolve());
                                }
                                resolve()
                            }, 1000)
                        }),
                    onRowUpdate: (newData, oldData) =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                {
                                    const data = this.state.data;
                                    const index = data.indexOf(oldData);
                                    data[index] = newData;
                                    this.setState({data}, () => resolve());
                                }
                                resolve()
                            }, 1000)
                        }),
                    onRowDelete: oldData =>
                        new Promise((resolve, reject) => {
                            setTimeout(() => {
                                {
                                    let data = this.state.data;
                                    const index = data.indexOf(oldData);
                                    data.splice(index, 1);
                                    this.setState({data}, () => resolve());
                                }
                                resolve()
                            }, 1000)
                        }),
                }}
            />
        )
    }
}

export default Editable;
