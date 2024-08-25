import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { createTask, deleteTask, updateTask, getTask } from "../api/task.api";
import { useNavigate, useParams } from "react-router-dom";
import {toast} from 'react-hot-toast'



export function TaskFormPage() {
    const { register, handleSubmit, setValue } = useForm();
    const navigate = useNavigate();
    const params = useParams();

    const onSubmit = handleSubmit(async data => {
        if (params.id) {
             updateTask(params.id, data)
             toast.success("Tarea actualizada", {position: "bottom-right", style:{
                background:"#101010",
                color: "#fff"
            }} );
        } else {
            await createTask(data);
            toast.success("Tarea creada", {position: "bottom-right", style:{
                background:"#101010",
                color: "#fff"
            }} );
        }
        navigate("/tasks");
    });

    useEffect (() =>{
        async function loadTask() {
            if (params.id) {
                const res = await getTask(params.id);
                setValue("title", res.data.title);
                setValue("decription", res.data.decription);
            }
        }
        loadTask()
        
    }, [])
    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit}>
                <input 
                    type="text" 
                    placeholder="Title"
                    {...register("title", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                <textarea 
                    rows="3" 
                    placeholder="Description"
                    {...register("decription", { required: true })} // Corregido
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                ></textarea>
                <button className='bg-indigo-500 px-3 py-2 rounded text-white block w-full mt-3'>Save</button>
            </form>

            {params.id && (
                <div className="flex justify-end"> 
                    <button
                    onClick={async () => {
                        const accepted = window.confirm("¿Desea eliminar?");
                        if (accepted) {
                            try {
                                await deleteTask(params.id);
                                toast.success("Tarea eliminada", {position: "bottom-right", style:{
                                    background:"#101010",
                                    color: "#fff"
                                }} );
                                navigate("/tasks");
                            } catch (error) {
                                console.error("Error al eliminar la tarea:", error);
                                alert("No se pudo eliminar la tarea. Inténtelo de nuevo.");
                            }
                        }
                    }}
                    className="bg-red-500 px-3 py-2 rounded text-white block w-48 mt-3"
                >
                    Delete
                </button>
                </div>
            )}
        </div>
    );
}
