const API_URL = 'http://127.0.0.1:8000/api/funcionarios/';

async function cargarFuncionarios() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        const tabla = document.getElementById('lista-funcionarios');
        tabla.innerHTML = '';

        data.forEach(f => {
            const techs = f.tecnologias.map(t => t.nombre).join(', ');

            tabla.innerHTML += `
                <tr>
                    <td>${f.nombre_completo}</td>
                    <td><span class="badge bg-info text-dark">${f.grado}</span></td>
                    <td>${techs}</td>
                </tr>
            `;
        });
    } catch (error) {
        console.error("Error cargando API:", error);
    }
}

cargarFuncionarios();