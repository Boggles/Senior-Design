using System.Collections;
using System.Collections.Generic;
using UnityEngine;
//using UnityEditor;
using System.IO;
//using System;


public class PointCloud : MonoBehaviour
{
    // Initialize Global File Reader Variables
    public TextAsset SF;
    public int scalefactor;
    protected StringReader reader = null;
    protected string text;

    private Mesh mesh;
    int numPoints = 35000;

    // Use this for initialization
    void Start()
    {
        // Set Reader Variables to text file
        //SF = (TextAsset)Resources.Load("Assets/Points_1.26.18.txt");
        reader = new StringReader(SF.text);
        Debug.Log(reader.ReadLine());
        // Initliaize Mesh
        mesh = new Mesh();
        GetComponent<MeshFilter>().mesh = mesh;
       
        CreateMesh();
        
    }

    /*void Update()
    {

        
    }*/

    void CreateMesh()
    {
        // Initialize Point Variables
        Vector3[] points = new Vector3[numPoints];
        int[] indecies = new int[numPoints];
        Color[] colors = new Color[numPoints];

        double[] temp_arr = new double[3];
        
        text = reader.ReadLine();
        int j = 0;
        // Read from File
        while (text != null)
        {
            char[] delimiter = { ' ' };
            string[] substrings = text.Split(delimiter, System.StringSplitOptions.RemoveEmptyEntries);
            int i = 0;
            foreach (string substring in substrings)
            {
                double x;
                substring.Trim();
                double.TryParse(substring, out x);
                temp_arr[i] = x;
                //Debug.Log(x);
                i++;
            }
            //Keep in mind TransformPoint for scaling, may be a better option for resizing at run time
            points[j] = new Vector3((float)temp_arr[0]/scalefactor, (float)temp_arr[1]/scalefactor, (float)temp_arr[2]/scalefactor); //50 might be the most accurate
            indecies[j] = j;
            colors[j] = new Color(0.14f, 1.0f, 0.23f, 0.0f); // color orange
            text = reader.ReadLine();
            j++;
        }

        // Set point values to mesh and plot
        mesh.vertices = points;
        mesh.colors = colors;
        mesh.SetIndices(indecies, MeshTopology.Points, 0);

    }

}