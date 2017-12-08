using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.IO;


public class PointCloud : MonoBehaviour
{
    // Initialize File Reader Variables
    protected FileInfo theSourceFile = null;
    protected StreamReader reader = null;
    protected string text = " "; // assigned to allow first line to be read below

    private Mesh mesh;
    int numPoints = 10000;

    // Use this for initialization
    void Start()
    {
        // Set Reader Variables to text file
        theSourceFile = new FileInfo("Assets/Points.txt");
        reader = theSourceFile.OpenText();

        // Initliaize Mesh
        mesh = new Mesh();
        GetComponent<MeshFilter>().mesh = mesh;
    }

    void Update()
    {

        // Read from File
        if (text != null)
        {
            text = reader.ReadLine();
            //Console.WriteLine(text);
            Debug.Log(text);
            CreateMesh();
        }
    }

    void CreateMesh()
    {
        // Initialize Point Variables
        Vector3[] points = new Vector3[numPoints];
        int[] indecies = new int[numPoints];
        Color[] colors = new Color[numPoints];

        // Loop to randomly plot points in a 20x20x20 cube
        for (int i = 0; i < numPoints; ++i)
        {
            points[i] = new Vector3(Random.Range(-10, 10), Random.Range(-10, 10), Random.Range(-10, 10));
            indecies[i] = i;
            colors[i] = new Color(0.0f, 0.0f, 1.0f, 1.0f); // color blue
        }

        // Set point values to mesh and plot
        mesh.vertices = points;
        mesh.colors = colors;
        mesh.SetIndices(indecies, MeshTopology.Points, 0);

    }

}